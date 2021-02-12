
/**
 * Write a description of class extraMath here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class ExtraMath
{
    // instance variables - replace the example below with your own
    private static double defaultAcceptableError = 0.0000001;


    /**
     * Returns whether a certain value is equal to a certain other value, within the bounds of acceptable error.
     *
     * @param  a  the first double value
     * @param  b  the second double value
     * @return    whether the values are within the acceptable error value
     */
    public static boolean erquals(double a,double b)
    {
        // put your code here
        return erquals(a,b,defaultAcceptableError);
    }
    public static boolean erquals(double a,double b, double acceptableError)
    {
        return Math.abs(a-b)<=acceptableError;
    }
}
