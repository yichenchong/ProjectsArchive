package AssignmentsQ;


/**
 * Write a description of class Assignment here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Assignment
{
    // instance variables - replace the example below with your own
    private String name;
    private String category;
    private double grade;

    /**
     * Constructor for objects of class Assignment
     */
    public Assignment(String name, String category, double grade)
    {
        this.name = name;
        this.category = category;
        this.grade = grade;
    }

    public String getName() {
        return name;
    }
    
    public String getCategory() {
        return category;
    }
    
    public double getGrade() {
        return grade;
    }
}
