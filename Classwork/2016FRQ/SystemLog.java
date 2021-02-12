import java.util.List;
import java.util.ArrayList;
import java.util.stream.*;
/**
 * Write a description of class SystemLog here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class SystemLog
{
    // instance variables - replace the example below with your own
    private List<LogMessage> messageList;

    /**
     * Constructor for objects of class SystemLog
     */
    public SystemLog(String str)
    {
        messageList = new ArrayList<LogMessage>();
        int start = 0;
        for(int i = 0; i < str.length(); i++) if(str.charAt(i)=='\n'){
            messageList.add(new LogMessage(str.substring(start,i)));
            start = i + 1;
        }
        messageList.add(new LogMessage(str.substring(start)));
    }

    
    public List<LogMessage> removeMessages(String keyword) {
        List<LogMessage> output = new ArrayList<LogMessage>();
        for(int i=0;i<messageList.size();i++) if(messageList.get(i).containsWord(keyword)) output.add(messageList.remove(i--));
        return output;
    }
}
