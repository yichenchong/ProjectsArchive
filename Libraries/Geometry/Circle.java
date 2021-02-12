
/**
 * Write a description of class Circle here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Circle
{
    // instance variables - replace the example below with your own
    private int radius;
    private Coordinate center;

    /**
     * Constructor for objects of class Circle
     */
    public Circle(Coordinate c, int r)
    {
        // initialise instance variables
        center = c;
        radius = r;
    }
    

    /**
     * returns whether a point is on the circumference of a circle
     *
     * @param  x  the coordinates of a point
     * @return    whether the point is on the circumference of a circle
     */
    public boolean pointOnCircle(Coordinate x)
    {
        LineSegment radiusLine = new LineSegment(this.center,x);
        return (ExtraMath.erquals(radiusLine.length(),this.radius));
    }
    public double radius()
    {
        return this.radius;
    }
    public Coordinate center()
    {
        return this.center;
    }
    
    /**
     * returns whether a point is in a circle
     *
     * @param  x  the coordinates of a point
     * @return    whether the point is in a circle
     */
    public boolean pointInCircle(Coordinate x)
    {
        LineSegment radiusLine = new LineSegment(this.center,x);
        return (radiusLine.length()<=this.radius);
    }
    public boolean intersects(Line line1)
    {
        return line1.intersects(this);
    }
    public boolean intersects(Circle circ)
    {
        LineSegment seg1 = new LineSegment(circ.center(),this.center());
        return seg1.length()<=circ.radius()+this.radius();
    }
}
