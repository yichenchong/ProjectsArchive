
/**
 * Write a description of class LogMessage here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class LogMessage
{
    // instance variables - replace the example below with your own
    private String machineId;
    private String description;

    /**
     * Constructor for objects of class LogMessage
     */
    public LogMessage(String message)
    {
        // initialise instance variables
        int colindex = message.indexOf(":");
        machineId = message.substring(0, colindex);
        description = message.substring(colindex);
    }

    public boolean containsWord(String keyword)
    {
        //return return (description.indexOf(keyword) != 1 && (description.indexOf(keyword) == 0 || description.charAt(index-1)==' ') && (description.indexOf(keyword)+keyword.length()==description.length()||description.charAt(description.indexOf(keyword)+keyword.length())==' '))||containsWord(keyword.substring(description.indexOf(keyword)+keyword.length()));
        int index = description.indexOf(keyword);
        return (index != -1 && (index == 0 || description.charAt(index-1)==' ') && (index+keyword.length()==description.length()||description.charAt(index+keyword.length())==' '))||containsWord(keyword.substring(index+keyword.length()));
    }
}
