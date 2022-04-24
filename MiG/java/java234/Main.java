import java.util.Hashtable;
import java.util.List;

public class Main{ 
    private static final String del = ";";
    private static final String pipedel = "\\|";
    private static final String pipeline = "|";
//const for simplification
    public static void main(String[] args) throws Exception {
        CsvProc proc = new CsvProc();
        List<List<String>> csvRawData = proc.readCsv("csv/csv_data_3.csv", del);
        Hashtable<String, String> dict = proc.dictFromCsv("csv/dictionary.txt", pipedel);
        List<List<String>> changedMethodsCsv = proc.intMethodsToStr(csvRawData, dict);
        System.out.println(changedMethodsCsv);
        proc.writeCsv("end/dictionarytext.csv", changedMethodsCsv, del);
        List<List<String>> turnedBr = proc.turnFigure(csvRawData, 6, 13.89);
        proc.writeCsv("end/turned.csv", turnedBr, pipeline);
        System.out.println(proc.brokenLineLength(csvRawData));
        System.out.println(proc.pointsQuantity(csvRawData));
    }
}