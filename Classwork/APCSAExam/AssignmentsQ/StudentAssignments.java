package AssignmentsQ;
import java.util.List;
import java.util.ArrayList;

/**
 * Write a description of class StudentAssignments here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class StudentAssignments
{
    // instance variables - replace the example below with your own
    List<Assignment> assignmentsList;

    // given in the exam
    /**
     * Constructor for objects of class StudentAssignments
     */
    public StudentAssignments(List<Assignment> assignmentsList)
    {
        // initialise instance variables
        this.assignmentsList = assignmentsList;
    }
    // given in the exam
    public List<String> getCategories() {
        List<String> output = new ArrayList<String>();
        for(Assignment a:assignmentsList) {
            boolean alrIn = false;
            for(String category:output) if(a.getCategory() == category) {
                alrIn = true;
                break;}
            if(!alrIn) output.add(a.getCategory());
        }
        return output;
    }
    
    public double getCategoryAvg(String cat) {
        double sum = 0, count = 0;
        for(Assignment a:assignmentsList) if(a.getCategory().equals(cat)) {
            sum += a.getGrade();
            count++;}
        return sum/count;
    }
    
    public String getHighestAvgCategory() {
        String max = getCategories().get(0);
        for (String cat:getCategories()) if(getCategoryAvg(cat)>getCategoryAvg(max)) max = cat;
        return max;
    }
}
