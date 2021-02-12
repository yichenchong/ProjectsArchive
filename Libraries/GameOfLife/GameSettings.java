
/**
 * Class that contains the settings for the game
 *
 * @author Yi Chen Chong
 * @version v0.0.1
 */
public class GameSettings
{
    // instance variables - replace the example below with your own
    private Matrix grid;
    private Rules r;
    private static int[] DEFAULT_BORN={3};
    private static int[] DEFAULT_SURVIVES={2,3};
    private static boolean DEFAULT_WRAP=false;
    private static int DEFAULT_ROWS=16;
    private static int DEFAULT_COLS=16;
    

    /**
     * Constructor for objects of class GameSettings
     */
    public GameSettings(int rows,int columns,boolean wraparound,int[] born,int[] survives)
    {
        grid=new Matrix(rows,columns,wraparound);
        r=new Rules(born,survives);
    }
    /**
     * Constructor for objects of class GameSettings
     */
    public GameSettings(int rows,int columns,boolean wraparound) {
        int[] born=DEFAULT_BORN;
        int[] survives=DEFAULT_SURVIVES;
        grid=new Matrix(rows,columns,wraparound);
        r=new Rules(born,survives);
    }
    /**
     * Constructor for objects of class GameSettings
     */
    public GameSettings(int rows,int columns,int[] born,int[] survives) {
        grid=new Matrix(rows,columns,DEFAULT_WRAP);
        r=new Rules(born,survives);
    }
    /**
     * Constructor for objects of class GameSettings
     */
    public GameSettings(int rows,int columns) {
        int[] born=DEFAULT_BORN;
        int[] survives=DEFAULT_SURVIVES;
        grid=new Matrix(rows,columns,DEFAULT_WRAP);
        r=new Rules(born,survives);
    }
    /**
     * Constructor for objects of class GameSettings
     */
    public GameSettings() {
        int[] born=DEFAULT_BORN;
        int[] survives=DEFAULT_SURVIVES;
        grid=new Matrix(DEFAULT_ROWS,DEFAULT_COLS,DEFAULT_WRAP);
        r=new Rules(born,survives);
    }
    
    /**
     * Method that returns the rules for the game
     * @returns the Rules object
     */
    public Rules rules() {
        return r;
    }
    /**
     * Method that returns the grid for the game
     * @returns a Matrix object
     */
    public Matrix grid() {
        return grid;
    }
}
