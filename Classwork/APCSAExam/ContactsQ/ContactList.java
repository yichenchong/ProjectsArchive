package ContactsQ;

import java.util.List;

/**
 * Write a description of class ContactList here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class ContactList
{
    private List<Contact> contactList;

    /**
     * Constructor for objects of class ContactList
     */
    public ContactList(List<Contact> contactList)
    {
        this.contactList = contactList;
    }
    
    public String toString(){
        String output = "";
        for(Contact c:contactList) output += c.toString() + "\n";
        return output;
    }
    
    public void changeNumber(String name, String number) {
        for(Contact c:contactList) if(c.getName().equals(name)) c.changeNumber(number);
    }
    
}
