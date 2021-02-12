
/**
 * Write a description of class RandomLetterChooser here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class RandomLetterChooser extends RandomStringChooser
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class RandomLetterChooser
     */
    public RandomLetterChooser(String str)
    {
        super(getSingleLetters(str));
    }
    public static String[] getSingleLetters(String str)
    {
        String[] output = new String[str.length()];
        for(int i = 0; i < str.length(); i++) output[i] = str.substring(i, i+1);
        return output;
    }
}
