import java.util.ArrayList;
import java.util.Scanner;

public class RedpacketCase {
    public static void main(String[] args){
        //make an instance of boss
        Boss boss = new Boss("John", 1000);

        //allow user to enter red packet value and quantity
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the total amount you want to give out");
        int money = sc.nextInt();
        System.out.println("Please enter the number of red packets you wish to give out");
        int count = sc.nextInt();

        //sending redpackets
        ArrayList<Double> packetList = boss.send(money,count);
        if (packetList == null){
            System.out.println("you don't have enough balance");
            return;
        }

        //create two members
        Member m1 = new Member("Member1",0);
        Member m2 = new Member("Member2",500);

        //open redpackets
        m1.OpenPacket(packetList);
        m2.OpenPacket(packetList);

        //check balance
        boss.show();
        m1.show();
        m2.show();

    }
}
