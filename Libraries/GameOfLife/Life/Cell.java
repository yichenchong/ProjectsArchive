
/**
 * Basic game units
 *
 * @author Yi Chen Chong
 * @version v0.0.1
 */
public class Cell
{
    private boolean alive;

    /**
     * Constructor for objects of class Cell
     */
    public Cell()
    {
        // initialise instance variables
        alive=false;
    }
    /**
     * Makes the cell living
     */
    public void isBorn() {
        alive=true;
    }
    /**
     * Makes the cell dead
     */
    public void dies() {
        alive=false;
    }
    /**
     * Gets the state of the cell
     * @returns whether the cell is alive
     */
    public boolean getState() {
        return alive;
    }
}
