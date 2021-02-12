package ContactsQ;


/**
 * Write a description of class Contact here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Contact
{
    // instance variables - replace the example below with your own
    private String name;
    private String number;

    /**
     * Constructor for objects of class Contact
     */
    public Contact(String name, String number)
    {
        this.name = name;
        this.number = number;
    }

    public String getName() {return name;}
    public String getNumber() {return number;}
    public void changeNumber(String newNumber) {number = newNumber;}
    public String toString() {return name + ": " + number;}
}
