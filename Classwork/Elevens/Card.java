
/**
 * Write a description of class Card here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Card
{
    // instance variables - replace the example below with your own
    private String rank;
    private String suit;
    private int pts;

    /**
     * Constructor for objects of class Card
     */
    public Card(String rank, String suit, int pts)
    {
        this.rank = rank;
        this.suit = suit;
        this.pts = pts;
    }

    /**
     * Gets point value of card
     *
     * @return    the point value of the card
     */
    public int getPointValue()
    {
        return pts;
    }
    public String getRank()
    {
        return rank;
    }
    public String getSuit()
    {
        return suit;
    }
    public boolean equals(Card other)
    {
        return other.getRank().equals(rank) && other.getSuit().equals(suit) && other.getPointValue() == pts;
    }
    public String toString() {
        return rank + " of " + suit + " (point value = " + pts + ")";
    }
    
}
