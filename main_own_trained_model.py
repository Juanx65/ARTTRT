import argparse
import os
import time

import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data

from utils.models.resnet import resnet18, resnet50, resnet101, resnet152
from utils.data_loader import data_loader
from utils.helper import AverageMeter, accuracy, adjust_learning_rate

train_on_gpu = torch.cuda.is_available()
if not train_on_gpu:
    print('CUDA is not available. Training on CPU')
else:
    print('CUDA is available. Training on GPU')

device = torch.device("cuda:0" if train_on_gpu else "cpu")

best_prec1 = 0.0

def main_train_eval(opt):
    global best_prec1, device
    
    if(opt.resnet50):
        model = resnet50()
    else:
        model = resnet18()
       
    model.to(device)

    # define loss and optimizer
    criterion = nn.CrossEntropyLoss().to(device)
    optimizer = optim.SGD(model.parameters(), lr=opt.lr,
                          momentum=opt.momentum,
                          weight_decay=opt.weight_decay)

    # Data loading
    train_loader, val_loader = data_loader(opt.dataset, opt.batch_size, opt.workers, opt.pin_memmory)

    if opt.evaluate:
        if opt.trt:
            from utils.engine import TRTModule #if not done here, unable to train
            current_directory = os.path.dirname(os.path.abspath(__file__))
            engine_path = os.path.join(current_directory,opt.weights)
            Engine = TRTModule(engine_path,device)
            Engine.set_desired(['outputs'])
            model = Engine
        else:    
            model = torch.load(opt.weights)
        model.to(device)

        validate(val_loader, model, criterion, opt.print_freq,opt.batch_size)
        return

    for epoch in range(0, opt.epochs):
        adjust_learning_rate(optimizer, epoch, opt.lr)

        # train for one epoch
        train(train_loader, model, criterion, optimizer, epoch, opt.print_freq,opt.batch_size)

        # evaluate on validation set
        prec1, prec5 = validate(val_loader, model, criterion, opt.print_freq,opt.batch_size)

        # remember the best prec@1 and save checkpoint
        is_best = prec1 > best_prec1
        best_prec1 = max(prec1, best_prec1)

        if is_best:
            torch.save(model, opt.weights)


def train(train_loader, model, criterion, optimizer, epoch, print_freq, batch_size):
    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()
    top5 = AverageMeter()

    # switch to train mode
    model.train()

    end = time.time()
    for i, (input, target) in enumerate(train_loader):

        if input.size(0) != batch_size:
            print(f"Deteniendo la evaluación. Tamaño del lote ({input.size(0)}) no es igual a batch_size ({batch_size}).")
            break

        # measure data loading time
        data_time.update(time.time() - end)

        target = target.to(device)#cuda(async=True)
        input = input.to(device)#cuda(async=True)

        # compute output
        output = model(input)
        loss = criterion(output, target)

        # measure accuracy and record loss
        prec1, prec5 = accuracy(output.data, target, topk=(1, 5))
        losses.update(loss.item(), input.size(0))
        top1.update(prec1[0], input.size(0))
        top5.update(prec1[0], input.size(0))

        # compute gradient and do SGD step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        if i % print_freq == 0:
            print('Epoch: [{0}][{1}/{2}]\t'
                  'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                  'Data {data_time.val:.3f} ({data_time.avg:.3f})\t'
                  'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                  'Prec@1 {top1.val:.3f} ({top1.avg:.3f})\t'
                  'Prec@5 {top5.val:.3f} ({top5.avg:.3f})\t'.format(
                epoch, i, len(train_loader), batch_time=batch_time,
                data_time=data_time, loss=losses, top1=top1, top5=top5))


def validate(val_loader, model, criterion, print_freq, batch_size):
    batch_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()
    top5 = AverageMeter()

    # switch to evaluate mode
    model.eval()

    end = time.time()
    for i, (input, target) in enumerate(val_loader):
        # Comprobar el tamaño del lote
        if input.size(0) != batch_size:
            print(f"Deteniendo la evaluación. Tamaño del lote ({input.size(0)}) no es igual a batch_size ({batch_size}).")
            break
        target = target.to(device)#cuda(async=True)
        input = input.to(device)#cuda(async=True)
        with torch.no_grad():
            # compute output
            output = model(input)
            loss = criterion(output, target)

            # measure accuracy and record loss
            prec1, prec5 = accuracy(output.data, target, topk=(1, 5))
            losses.update(loss.item(), input.size(0))
            top1.update(prec1[0], input.size(0))
            top5.update(prec5[0], input.size(0))

            # measure elapsed time
            batch_time.update(time.time() - end)
            end = time.time()

            if i % print_freq == 0:
                print('Test: [{0}/{1}]\t'
                      'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                      'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                      'Prec@1 {top1.val:.3f} ({top1.avg:.3f})\t'
                      'Prec@5 {top5.val:.3f} ({top5.avg:.3f})'.format(
                    i, len(val_loader), batch_time=batch_time, loss=losses,
                    top1=top1, top5=top5))

    print(' * Prec@1 {top1.avg:.3f} Prec@5 {top5.avg:.3f}'.format(top1=top1, top5=top5))
    print(' * Average Time Per Batch {batch_time.avg:.3f}'.format(batch_time=batch_time))

    return top1.avg, top5.avg


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', default='dataset/', help='path to dataset')
    parser.add_argument('--batch_size', default = 256, type=int,help='batch size to train')
    parser.add_argument('--epochs', default = 90, type=int,help='epoch to train')
    parser.add_argument('--weight-decay', '--wd', default=1e-4, type=float, help='Weight decay (default: 1e-4)')
    parser.add_argument('--momentum', default = 0.9, type=float,help='momentum')
    parser.add_argument('--lr', default = 0.01, type=float, help='learning rate')
    parser.add_argument('--weights', default = 'weights/best.pth', type=str, help='directorio y nombre de archivo de donse se guardara el mejor peso entrenado')
    parser.add_argument('-m','--pin_memmory', action='store_true',help='use pin memmory')
    parser.add_argument('-j', '--workers', default=4, type=int, help='number of data loading workers (default: 4)')
    parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',help='evaluate model on validation set')
    parser.add_argument('--print-freq', '-f', default=10, type=int, metavar='N',help='print frequency (default: 10)')
    parser.add_argument('-trt','--trt', action='store_true',help='evaluate model on validation set al optimizar con tensorrt')
    parser.add_argument('-rn50','--resnet50', action='store_true',help='use ResNet50 as model')
    parser.add_argument('-rn18','--resnet18', action='store_true',help='use ResNet18 as model')

    opt = parser.parse_args()
    return opt

def main(opt):
    main_train_eval(opt)

if __name__ == '__main__':
    opt = parse_opt()
    main(opt)