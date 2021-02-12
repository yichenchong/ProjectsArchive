
/**
 * Write a description of class LineSegment here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class LineSegment
{
    // instance variables - replace the example below with your own
    private double startX;
    private double startY;
    private double endX;
    private double endY;
    private double slope;
    private double angle;

    /**
     * Constructor for objects of class LineSegment
     */
    public LineSegment(Coordinate start, Coordinate end)
    {
        // initialise instance variables
        startX = start.getX();
        startY = start.getY();
        endX = end.getX();
        endY = end.getY();
        if(startY==endY) {
            slope = 0;
            angle = 0;
        }
        else if(startX!=endX) {
            angle = Math.atan((startY-endY)/(startX-endX));
            slope = (startY-endY)/(startX-endX);
        }
        else {
            angle = Math.PI;
            slope = 3E100;
        }
    }
    

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public double slope()
    {
        return this.slope;
    }
    
    public double length()
    {
        double deltaY=this.endY-this.startY;
        double deltaX=this.endX-this.startX;
        return Math.pow(Math.pow(deltaY,2)+Math.pow(deltaX,2),0.5);
    }
    
    public Line makeLine(){
        return new Line(new Coordinate(startX,startY), new Coordinate(endX,endY));
    }
    
    public boolean pointOnSegment(Coordinate test)
    {
        double testX = test.getX();
        double testY = test.getY();
        boolean xInRange = (testX<=this.endX&&testX>=this.startX)||(testX>=this.endX&&testX<=this.startX);
        boolean yInRange = (testY<=this.endY&&testY>=this.startY)||(testY>=this.endY&&testY<=this.startY);
        if(!xInRange||!yInRange) return false;
        double yAtX = this.slope()*(testX-this.startX)+this.startY;
        return ExtraMath.erquals(yAtX,test.getY());
    }
    
    public Coordinate pointFromStart(double dist)
    {
        double xCoord,yCoord;
        if(dist>this.length()) throw new RuntimeException();
        double distX=dist/Math.pow(1+Math.pow(this.slope(),2),0.5);
        double distY=distX*this.slope();
        if(this.startX<this.endX) {
            xCoord=this.startX+distX;
            yCoord=this.startY+distY;
        }
        else if(this.startX>this.endX) {
            xCoord=this.startX-distX;
            yCoord=this.startY-distY;
        }
        else if (this.startY>this.endY) {
            xCoord=this.startX-distX;
            yCoord=this.startY-distY;
        }
        else {
            xCoord=this.startX+distX;
            yCoord=this.startY+distY;
        }
        return new Coordinate(xCoord,yCoord);
    }
    public Coordinate midpoint()
    {
        return new Coordinate((this.startX+this.endX)/2,(this.startY+this.endY)/2);
    }
    
}
