import re
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


if __name__=='__main__':
    file = open('./logs/log.txt','r')
    #file = open('./logs/log_cardinality2.txt','r')
    #file = open('./logs/log_cardinality2_LR01.txt','r')
    accuracy = []
    epochs = []
    loss = []
    test_loss_vec = []
    for line in file:
        test_accuracy = re.search('"test_accuracy": ([0]\.[0-9]+)*', line)
        if test_accuracy:
            if type(float(test_accuracy.group(1))) == str:
                accuracy.append(float(test_accuracy.group(1)))
            else:
                accuracy.append(test_accuracy.group(1))
        
        epoch = re.search('"epoch": ([0-9]+)*', line)
        if epoch:
            epochs.append(epoch.group(1))
        
        train_loss = re.search('"train_loss": ([0-9]\.[0-9]+)*', line)
        if train_loss:
            if type(train_loss.group(1)) == str:
                loss.append(float(train_loss.group(1)))
            else:
                loss.append(train_loss.group(1)) 

        test_loss = re.search('"test_loss": ([0-9]\.[0-9]+)*', line)
        if test_loss:
            if type(test_loss.group(1)) == str:
                test_loss_vec.append(float(test_loss.group(1)))
            else:
                test_loss_vec.append(test_loss.group(1))
            
    file.close()
    fig1=plt.figure('test_accuracy vs epochs')  
    ax = fig1.add_subplot(2,1,1)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xlabel('epoch')
    plt.ylabel('test_accuracy')
    plt.plot(epochs,accuracy,'b*')
    plt.plot(epochs,accuracy,'r')
    plt.grid(True)
    fig1.savefig("TestAccuracy.png")

    fig2=plt.figure('train_loss vs epochs')
    plt.xlabel('epoch')
    plt.ylabel('train_loss')
    plt.plot(epochs,loss,'b*')
    plt.plot(epochs,loss,'y')
    plt.grid(True)
    fig2.savefig("LossVsEpoch.png")


    fig3=plt.figure('test_loss vs epochs')
    plt.xlabel('epoch')
    plt.ylabel('test_loss')
    plt.plot(epochs,test_loss_vec,'b*')
    plt.plot(epochs,test_loss_vec,'y')
    plt.grid(True)
    fig3.savefig("TestLossVsEpoch.png")
   
    plt.show()
    
