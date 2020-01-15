import java.util.ArrayList;
import java.util.Random;

public class Member extends User{
    public Member(){};
    public Member(String username, double balance){
        super(username, balance);
    };

    public void OpenPacket(ArrayList<Double> packetList){
        //randomly generate an index for the packet list
        Random r = new Random();
        int index = r.nextInt(packetList.size());

        double packetMoney = packetList.remove(index);
        setBalance(packetMoney+super.getBalance());

    }
}
