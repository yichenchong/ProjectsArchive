
/**
 * Write a description of class CardTester here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class CardTester
{
    public static void main(String[] args) {
        Card a = new Card("jack", "hearts", 10);
        Card b = new Card("queen", "diamonds", 11);
        Card c = new Card("jack", "hearts", 10);
        
        System.out.println(a.getRank());
        System.out.println(b.getSuit());
        System.out.println(c.getPointValue());
        
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        
        System.out.println(a.equals(b) + " " + b.equals(c) + " " + c.equals(a));
        
    }
}
