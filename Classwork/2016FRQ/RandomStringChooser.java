import java.util.ArrayList;
import java.util.List;
/**
 * Write a description of class RandomStringChooser here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class RandomStringChooser
{
    // instance variables - replace the example below with your own
    private List<String> wordList;

    /**
     * Constructor for objects of class RandomStringChooser
     */
    public RandomStringChooser(String[] wordArray){
        // initialise instance variables
        wordList = new ArrayList<String>();
        for(String i:wordArray) wordList.add(i);
    }
    
    public String getNext() {
        return (wordList.size()==0)?"NONE":(wordList.remove((int)(Math.random()*wordList.size())));
    }
    
}
