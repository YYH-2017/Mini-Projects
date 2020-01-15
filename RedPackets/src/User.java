public class User {
    private String username;
    private double balance;

    public User(){}
    public User(String username, double balance) {
        this.username = username;
        this.balance = balance;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    //method to display account info
    public void show(){
        System.out.println("User: "+username+" , balance: " + balance + " $");
    }
}
