import java.util.ArrayList;

public class Boss extends User {
    public Boss(){}
    public Boss(String username, double balance){
        //uses parent's constructor
        super(username,balance);
    }

    /*
    boss sends red packet in integer and divided into many
    packets
    1. needs to get the balance of the boss see if its enough
    to send the packet
    2.update the balance of the boss
    3.divide packet into even amount,if not even, remain will be
    added to the last packet
     */

    public ArrayList<Double> send (int packetAmount, int count){
        //gets balance from the boss
        double balance = getBalance();
        if(packetAmount > balance){
            return null;
        }

        //update boss's balance
        setBalance(balance-packetAmount);

        //create a list to store the packet amount
        ArrayList<Double> packetList = new ArrayList<>();

        //calculate per packet amount
        int perPacketAmount = packetAmount / count;
        int remainder = packetAmount % count;

        //divide into n-1 packets for the same amount
        //leaving the last packet to have the remainder

        for (int i = 0;i<count-1;i++){
            packetList.add((double)perPacketAmount);
        }

        //check if there is remainder
        if(remainder == 0){
            packetList.add((double)perPacketAmount);
        }else{
            packetList.add((double)perPacketAmount+remainder);
        }
        return packetList;

    }
}
