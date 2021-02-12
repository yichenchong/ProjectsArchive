

/**
 * A grid to store the game in
 *
 * @author Yi Chen Chong
 * @version v0.0.1
 */
public class Matrix
{
    // instance variables - replace the example below with your own
    private Cell[][] grid;
    private boolean wraparound;

    /**
     * Constructor for objects of class Matrix
     */
    public Matrix(int rows,int columns,boolean wraparound)
    {
        // initialise instance variables
        grid=new Cell[rows][columns];
        this.wraparound=wraparound;
        for(int i=0;i<grid.length;i++) for(int j=0;j<grid[i].length;j++) grid[i][j]=new Cell();
    }
    
    /**
     * A method to create a living cell at the location specified.
     * @param row the row of the specified location
     * @param col the column of the specified location
     */
    public void add(int row,int column) {
        grid[row][column].isBorn();
    }
    /**
     * A method to remove a living cell from the specified location.
     * @param row the row of the specified location
     * @param col the column of the specified location
     */
    public void delete(int row,int column) {
        grid[row][column].dies();
    }
    /**
     * A method to get the number of living neighbours a cell has.
     * @param row the row of the cell
     * @param column the column of the cell
     * @returns the number of living neighbours
     */
    public int getNeighborhood(int row,int column) {
        int count=0;
        for(int i=-1;i<2;i++) for(int j=-1;j<2;j++) {
            try {
                if(grid[row+i][column+j].getState()&&(i!=0||j!=0)) {
                    count++;
                }
            }
            catch(ArrayIndexOutOfBoundsException d) {
                if(wraparound) {
                    int tempRow=row+i,tempColumn=row+j;
                    if(tempRow<0)tempRow=grid.length-1;
                    if(tempColumn<0)tempRow=grid[0].length-1;
                    if(tempRow==grid.length) tempRow=0;
                    if(tempColumn==grid[0].length) tempColumn=0;
                    if(grid[tempRow][tempColumn].getState()) count++;
                }
            }
        }
        return count;
    }
    /**
     * returns the state of the cell at a certain location
     * @param row the row of the cell
     * @param column the column of the cell
     * @returns whether the cell is alive
     */
    public boolean getState(int row,int column) {
        return grid[row][column].getState();
    }
    /**
     * Gets the size of the matrix
     * @returns an array of length 2 representing the matrix's rows and columns.
     */
    public int[] gridSize() {
        int[] output= {grid.length,grid[0].length};
        return output;
    }
    /**
     * Gets whether the matrix is wrapped around
     * @returns whether wraparound is selected
     */
    public boolean wrap() {
        return wraparound;
    }
}
