
/**
 * Write a description of class Crossword here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Crossword
{
    // instance variables - replace the example below with your own
    private Square[][] puzzle;

    /**
     * Constructor for objects of class Crossword
     */
    public Crossword(boolean[][] blackSquares)
    {
        // initialise instance variables
        puzzle = new Square[blackSquares.length][blackSquares[0].length];
        int count = 1;
        for(int i = 0; i < puzzle.length; i++) for(int j = 0; j< puzzle[i].length; j++) puzzle[i][j] = new Square(blackSquares[i][j], (toBeLabeled(i, j, blackSquares))?(count++):0);
        
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public boolean toBeLabeled(int r, int c, boolean[][] blackSquares)
    {
        return !blackSquares[r][c]&&(r==0||c==0||blackSquares[r-1][c]||blackSquares[r][c-1]);
        
    }
}
