import java.util.ArrayList;
import java.util.Random;

/**
 * Write a description of class Deck here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Deck
{
    // instance variables - replace the example below with your own
    private ArrayList<Card> cards;
    public int size;
    
    private static String[] STANDARD_RANKS = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",};
    private static String[] STANDARD_SUITS = {"Hearts", "Diamonds", "Spades", "Clovers"};
    private static int[] STANDARD_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 100, 100};

    /**
     * Constructor for objects of class Deck
     */
    public Deck(String[] ranks, String[] suits, int[] values)
    {
        cards = new ArrayList<Card>();
        
        for (String suit:suits) {
            for (int i = 0; i < ranks.length; i++) {
                String rank = ranks[i];
                int value = values[i];
                Card newCard = new Card(rank, suit, value);
                cards.add(newCard);
                size = cards.size();
                shuffle();
            }
        }
    }
    
    public Deck()
    {
        this(STANDARD_RANKS, STANDARD_SUITS, STANDARD_VALUES);
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    public int size() {
        return size;
    }
    public Card deal() {
        size--;
        return cards.get(size);
    }
    public void shuffle() {
        cards = shuffle(cards);
    }
    private ArrayList<Card> shuffle(ArrayList<Card> set) {
        if(set.size()<2) return set;
        
        ArrayList<Card> set1 = new ArrayList<Card>();
        ArrayList<Card> set2 = new ArrayList<Card>();
        
        for (int i = 0; i < set.size(); i++) {
            if (i <= set.size()/2) set1.add(set.get(i));
            else set2.add(set.get(i));
        }
        
        set1 = shuffle(set1);
        set2 = shuffle(set2);
        
        ArrayList<Card> finalSet = new ArrayList<Card>();
        Random rng = new Random();
        boolean value = rng.nextBoolean();
        
        if(value) {
            for (Card i:set1) finalSet.add(i);
            for (Card i:set2) finalSet.add(i);
        }
        else {
            for (Card i:set2) finalSet.add(i);
            for (Card i:set1) finalSet.add(i);
        }
        
        return finalSet;
    }
}
