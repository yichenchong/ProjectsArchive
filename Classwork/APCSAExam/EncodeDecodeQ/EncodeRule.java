package EncodeDecodeQ;


/**
 * Write a description of class EncodeRule here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class EncodeRule
{
    // instance variables - replace the example below with your own
    private String[] ruleArray;

    /**
     * Constructor for objects of class EncodeRule
     */
    public EncodeRule(String[] ruleArray)
    {
        this.ruleArray = ruleArray;
    }

    public String encodeLetter(String letter, boolean encode) {
        for(String rule:ruleArray) if(rule.indexOf(letter)!=-1) return encode?rule.charAt((rule.indexOf(letter)+1)%rule.length())+"":(rule.indexOf(letter)==0?rule.charAt(rule.length()-1)+"":rule.charAt(rule.indexOf(letter)-1)+"");
        //I'm stupid, but the following line works too:
        //for(String rule:ruleArray) if(rule.indexOf(letter)!=-1) return encode?rule.charAt((rule.indexOf(letter)+1)%rule.length())+"":rule.charAt((rule.indexOf(letter)+rule.length()-1)%rule.length())+"";
        return letter;
    }
    public String encodeWord(String word, boolean encode) {
        String out = "";
        for(int i = 0; i < word.length(); i++) out += encodeLetter(word.substring(i,i+1), encode);
        return out;
    }
}
