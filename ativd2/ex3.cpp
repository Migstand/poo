#include <iostream>
using namespace std;

class Conta{
    public:
    string titular;
    string numero;
    double saldo;
    Conta(){
        titular = "sem nome";
        numero = "sem número";
        saldo = 0;
    }
    void depositar(double valor) {
        saldo += valor;
    }
    void sacar(double valor){
        saldo -= valor;
    }
};

int main(){
    Conta x; // x é a instância
    Conta &y = x;
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    x.titular = "Raquel";
    x.numero = "123-x";
    x.saldo = 1000;
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    x.depositar(500);
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    y.depositar(1000);
    cout << y.titular << " " << y.numero << " " << y.saldo << endl;
    return 0;
}