import numpy as np
import torch
import torch.nn as nn
import torch.nn.init as init
import time
from torchinfo import summary

train_on_gpu = torch.cuda.is_available()
if not train_on_gpu:
    print('CUDA is not available.')
else:
    print('CUDA is available.')

global device
device = torch.device("cuda:0" if train_on_gpu else "cpu")

class ReLUNet(nn.Module):
    def __init__(self, num_layers=18, num_classes=1000):
        super(ReLUNet, self).__init__()
        
        # Inicializar módulos de la red
        layers = []

        for _ in range(num_layers):
            layers.append(nn.ReLU())

        self.relu_layers = nn.Sequential(*layers)

    def forward(self, x):
        x = self.relu_layers(x)
        return x

class CustomNet(nn.Module):
    def __init__(self, nx, M, nu, L):
        super(CustomNet, self).__init__()
        self.layers = nn.ModuleList()
        self.layers.append(nn.Linear(nx, M))
        self.layers.append(nn.ReLU(inplace=True))
        
        for _ in range(L-1):
            self.layers.append(nn.Linear(M, M))
            self.layers.append(nn.ReLU(inplace=True))
        
        self.layers.append(nn.Linear(M, nu))

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    
    def inicializar_pesos(self):
        for layer in self.layers:
            if hasattr(layer, 'weight'):
                init.xavier_uniform_(layer.weight)

def evaluate(model, nx, M, nu, L, batch_size=1):

    model.to(device)
    #summary(model, (3,224,224))
    #summary(model, (batch_size, nx))

    num_batches = 10000
    total_time = 0
    max_time = 0 # Inicializa la variable para el tiempo máximo}
    
    np_seed = 42
    np.random.seed(np_seed)
    inputs = np.random.rand(num_batches, nx)

    for i in range(num_batches):
        
        #torch.manual_seed(i)
        #input = torch.rand(batch_size, 3, 224, 224)
        #input = torch.rand(batch_size, nx)

        input = torch.from_numpy(inputs[i]).float() 

        start_time = time.time()
        input = input.to(device)
        with torch.no_grad():
            output = model(input)
            torch.cuda.synchronize()  # Asegura que todas las operaciones en la GPU se han completado
            output = output.cpu()
        end_time = time.time()

        cycle_time = end_time - start_time
        total_time += cycle_time

        if cycle_time > max_time:  # Comprueba si el tiempo del ciclo actual es el máximo hasta ahora
            max_time = cycle_time

    average_time = total_time / num_batches
    print(f"Vanilla {average_time} | {max_time} segundos")
    return

# Crear una instancia de la red
#nx, M, nu, L = entradas, neuronas x capa, salidas, Capas
nx, nu = 2, 1
L, M = 10, 5

#net = ReLUNet()
net = CustomNet(nx, M, nu, L)
net.inicializar_pesos()
net.to(device)
#torch.save(net, 'best.pth')

evaluate(net,nx, M, nu, L)

""" 
from engine import TRTModule 
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
engine_path = os.path.join(current_directory,"best.engine")

Engine = TRTModule(engine_path, device)
Engine.set_desired(['outputs'])
evaluate(Engine,nx, M, nu, L)
 """