
/**
 * Write a description of class Geometry here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Geometry
{

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static void main(String[] args)
    {
        // put your code here
        Coordinate circCenter = new Coordinate(3,5);
        Coordinate coord1 = new Coordinate(2,0);
        Coordinate coord2 = new Coordinate(-2,0);
        Line lineTest = new Line(coord1,coord2);
        Circle circTest = new Circle(circCenter,4);
        System.out.println(lineTest.intersects(circTest));
    }
}
