class Conta{
    public string titular
    public string numero
    public double saldo
    public Conta(){
        titular = "sem nome"
        numero = "sem número"
        saldo = 0
    }
    public void depositar(double valor) {
        saldo += valor
    }
    public void sacar(double valor){
        saldo -= valor
    }
}

public class ex3{
    public static void main(String[] args){
        Conta x = new Conta(); 
        x.titular = "Raquel"
        x.numero = "123-x"
        x.saldo = 1000
        system.out.print("Teste");
    }
}
