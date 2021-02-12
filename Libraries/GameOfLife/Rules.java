
/**
 * Stores a rule variation for the game of life
 *
 * @author Yi Chen Chong
 * @version v0.0.1
 */
public class Rules
{
    // instance variables - replace the example below with your own
    private int[] born;
    private int[] survives;

    /**
     * Constructor for objects of class Rules
     */
    public Rules(int[] born,int[] survives)
    {
        // initialise instance variables
        this.born=born;
        this.survives=survives;
    }
    public int[] bornRules() {
        return born;
    }
    public int[] surviveRules() {
        return survives;
    }
    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public String toString()
    {
        // put your code here
        String b="B";
        for(int i=0;i<born.length;i++) b+=born[i];
        String s="S";
        for(int i=0;i<survives.length;i++) s+=survives[i];
        return b+"/"+s;
    }
}
