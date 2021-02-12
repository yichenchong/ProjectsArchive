
/**
 * The Coordinate class creates a point in a Coordinate plane.
 *
 * @author Yi Chen Chong
 * @version 1.0.0
 */
public class Coordinate
{
    // instance variables - replace the example below with your own
    private double x;
    private double y;
    /**
     * Constructor for objects of class Coordinate
     */
    public Coordinate(double xInput, double yInput)
    {
        x = xInput;
        y = yInput;
    }
    

    /**
     * returns the x coordinate of the coordinate pair
     * @return    the x coordinate
     */
    public double getX()
    {
        return this.x;
    }
    
    /**
     * returns the y coordinate of the coordinate pair
     * @return    the y coordinate
     */
    public double getY()
    {
        return this.y;
    }
    
    /**
     * returns the x and y coordinates of the coordinate pair as an array
     * @return    the coordinate pair as an array
     */
    public double[] getCoord()
    {
        return new double[] {this.x,this.y};
    }
    
    public double[] getPolar()
    {
        double r = Math.pow(Math.pow(this.x,2)+Math.pow(this.y,2),0.5);
        double theta = Math.atan(this.y/this.x);
        if(this.y<0) theta+=Math.PI;
        double[] polarCoords = new double[] {r,theta};
        return polarCoords;
    }
    
    public static void printPoint(Coordinate point)
    {
        System.out.println("("+point.getX()+","+point.getY()+")");
    }
    public void printPoint()
    {
        System.out.println("("+this.getX()+","+this.getY()+")");
    }
    
    public boolean equals(Coordinate other)
    {
        return this.x==other.getX()&&this.y==other.getY();
    }
}
