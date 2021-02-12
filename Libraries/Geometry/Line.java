
/**
 * Write a description of class Line here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Line
{
    // instance variables - replace the example below with your own
    private double slope;
    private double yIntercept;
    private double angle;
    private double xIntercept;

    /**
     * Constructor for objects of class Line
     */
    public Line(double m, double b)
    {
        // initialise instance variables
        slope = m;
        yIntercept = b;
        xIntercept = -b/m;
        angle = Math.atan(m);
    }
    public Line(Coordinate point1, Coordinate point2)
    {
        // initialise instance variables
        if(point1.getY()==point2.getY()) {
            slope = 0;
            angle = 0;
            yIntercept = point1.getY();
        }
        else if(point1.getX()!=point2.getX()) {
            angle = Math.atan((point1.getY()-point2.getY())/(point1.getX()-point2.getX()));
            slope = (point1.getY()-point2.getY())/(point1.getX()-point2.getX());
            yIntercept = point1.getY()-slope*point1.getX();
            xIntercept = -yIntercept/slope;
        }
        else {
            angle = Math.PI;
            slope = 3E100;
            xIntercept = point1.getX();
        }
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public boolean onLine(Coordinate test)
    {
        // put your code here
        double testX = test.getX();
        double testY = test.getY();
        if(this.slope!=3E100) {
            double yAtX = this.slope*(testX)+this.yIntercept;
            return ExtraMath.erquals(yAtX,testY);
        }
        else {
            return this.xIntercept==testX;
        }
    }
    
    public double slope()
    {
        return this.slope;
    }
    
    public double angle()
    {
        return this.angle;
    }
    public double angle(Line other)
    {
        return Math.abs(this.angle-other.angle());
    }
    
    public double yAtX(double x) {
        if(this.slope>=3E100&&x!=this.xIntercept) {
            throw new RuntimeException();
        }
        else {
            return this.slope*(x)+this.yIntercept;
        }
    }
    
    public LineSegment createSegment(double x1,double x2) 
    {
        double y1=yAtX(x1);
        double y2=yAtX(x2);
        Coordinate coord1= new Coordinate(x1,y1);
        Coordinate coord2= new Coordinate(x2,y2);
        return new LineSegment(coord1,coord2);
    }
    public LineSegment createSegment(Coordinate coord, double len)
    {
        double distX=len/Math.pow(1+Math.pow(this.slope(),2),0.5);
        double distY=distX*this.slope();
        double xCoord = coord.getX()+distX;
        double yCoord = coord.getX()+distY;
        Coordinate point2 = new Coordinate(xCoord,yCoord);
        return new LineSegment(coord,point2);
    }
    
    public boolean intersects(Line other) {
        return this.slope!=other.slope();
    }
    public boolean intersects(LineSegment other) {
        boolean slopesEqual = other.slope()==this.slope;
        boolean startOnPlus,endOnPlus,startOrEndOnLine;
        Coordinate segStart = other.pointFromStart(0);
        Coordinate segEnd = other.pointFromStart(other.length());
        if(this.slope<3E100) {
            startOnPlus = segStart.getY()>this.yAtX(segStart.getX());
            endOnPlus = segEnd.getY()>this.yAtX(segEnd.getX());
            startOrEndOnLine = segStart.getY()==yAtX(segStart.getX())||segEnd.getY()==yAtX(segEnd.getX());
        }
        else {
            startOnPlus = segStart.getX()>this.xIntercept;
            endOnPlus = segEnd.getX()>this.xIntercept;
            startOrEndOnLine = segStart.getX()==xIntercept||segEnd.getX()==xIntercept;
        }
        return ((startOrEndOnLine)||((startOnPlus&&!endOnPlus)||(!startOnPlus&&endOnPlus)));
    }
    public boolean intersects(Circle circ) {
        double perpSlope, deltaX, deltaY;
        if(this.slope>=3E100) {
            perpSlope = 0;
            deltaX = circ.radius();
            deltaY = 0;
        }
        else if(this.slope==0) {
            perpSlope = 3E100;
            deltaX = 0;
            deltaY = circ.radius();
        }
        else {
            perpSlope = -1/this.slope;
            deltaX = Math.sqrt(Math.pow(circ.radius(),2)/(1+Math.pow(perpSlope,2)));
            deltaY = perpSlope * deltaX;
        }
        double centerX = circ.center().getX();
        double centerY = circ.center().getY();
        Coordinate point1 = new Coordinate(centerX-deltaX,centerY-deltaY);
        Coordinate point2 = new Coordinate(centerX+deltaX,centerY+deltaY);
        LineSegment seg = new LineSegment(point1,point2);
        
        return this.intersects(seg);
    }
}
    
    
