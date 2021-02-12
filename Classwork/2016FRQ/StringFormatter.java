import java.util.List;
import java.util.ArrayList;
/**
 * Write a description of class StringFormatter here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class StringFormatter
{
    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static int totalLetters(List<String> wordList)
    {
        int count = 0;
        for(String word:wordList) count += word.length();
        return count;
    }
    
    public static int basicGapWidth(List<String> wordList, int formattedLen) {
        return (formattedLen - totalLetters(wordList))/(wordList.size()-1);
    }
    
    public static int leftoverSpaces(List<String> wordList, int formattedLen) {
        return formattedLen - totalLetters(wordList) - basicGapWidth(wordList, formattedLen);
    }
    
    public static String format(List<String> wordList, int formattedLen) {
        int leftOver = leftoverSpaces(wordList, formattedLen);
        String basicGap = "", output = "";
        for(int i = 0; i< basicGapWidth(wordList, formattedLen);i++) basicGap += " ";
        for(String i:wordList) output += i + basicGap + ((leftOver-- > 0)?" ":"");
        return output.substring(0, output.length()-1);
    }
}
