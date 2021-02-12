package GraduationQ;
import java.util.List;
import java.util.ArrayList;

/**
 * Write a description of class Graduation here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Graduation
{
    List<String> lineRight;
    List<String> lineLeft;
    public Graduation() {
        lineRight = new ArrayList<String>();
        lineLeft = new ArrayList<String>();
    }
    public static void fillSeats(String[][] seats, List<String> studentList) {
        for(int i = 0; i < studentList.size(); i++) seats[i/seats[0].length][i%seats[0].length] = studentList.get(i);
    }
    public void addLineRight(String[] row) {
        for(String s:row) if(s != null) lineRight.add(s);
    }
    public void addLineLeft(String[] row) {
        for(String s:row) if(s != null) lineLeft.add(0,s);
    }
    public void fillLines(String[][] seats) {
        for(int i = 0; i < seats.length; i++) if(i%2==0) addLineRight(seats[i]);
        else addLineLeft(seats[i]);
    }
    
}




