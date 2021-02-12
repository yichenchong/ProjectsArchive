

/**
 * Class controlling the Game of Life game.
 *
 * @author Yi Chen Chong
 * @version v0.0.1
 */
public class Game
{
    // instance variables - replace the example below with your own
    private int turns;
    private GameSettings settings;
    public Matrix grid;

    /**
     * Constructor for objects of class Game, with a settings object passed in.
     */
    public Game(GameSettings set) {
        settings=set;
        grid=settings.grid();
        turns=0;
    }
    /**
     * Default constructor for objects of class Game
     */
    public Game()
    {
        settings=new GameSettings();
        grid=settings.grid();
        turns = 0;
    }
    /**
     * Moves on to next turn, processing the survival, birth, and death of each cell.
     */
    public void nextTurn() {
        int[] bornRules=settings.rules().bornRules();
        int[] surviveRules=settings.rules().surviveRules();
        Matrix newGrid=new Matrix(grid.gridSize()[0],grid.gridSize()[1],grid.wrap());
        for(int i=0;i<grid.gridSize()[0];i++) {
            for(int j=0;j<grid.gridSize()[1];j++) {
                int num=grid.getNeighborhood(i,j);
                boolean alive=grid.getState(i,j);
                if(alive&&inRules(surviveRules,num)) newGrid.add(i,j);
                else if(!alive&&inRules(bornRules,num)) newGrid.add(i,j);
            }
        }
        grid=newGrid;
    }
    /**
     * Simple helper method to return whether a number conforms to a rule array.
     * 
     * @param rules rule array, contains numbers to check against.
     * @param num number to see whether it is contained within the rules array.
     */
    private boolean inRules(int[] rules,int num) {
        for(int i=0;i<rules.length;i++) if(rules[i]==num) return true;
        return false;
    }
    
    /**
     * A method to create a living cell at the location specified.
     * @param row the row of the specified location
     * @param col the column of the specified location
     */
    public void add(int row,int col) {
        grid.add(row,col);
    }
    
    /**
     * A method to remove a living cell from the specified location.
     * @param row the row of the specified location
     * @param col the column of the specified location
     */
    public void delete(int row,int col) {
        grid.delete(row,col);
    }
    
    /**
     * A method to return the state of a cell at a particular location.
     * @param row the row of the location
     * @param col the column of the location
     */
    public boolean getState(int row,int col) {
        return grid.getState(row,col);
    }
}
