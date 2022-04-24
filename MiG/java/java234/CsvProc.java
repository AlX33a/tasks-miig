import java.util.*;
import java.util.stream.Collectors;
import java.text.NumberFormat;
import java.text.ParseException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class CsvProc {

    public List<List<String>> readCsv(String path, String delimiter) throws IOException {
        List<List<String>> records = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(delimiter);
                records.add(Arrays.asList(values));
            }
            records.removeIf(p -> p.isEmpty());
            return records;
        }
    }

    public void writeCsv(String path, List<List<String>> records, String delimiter) throws IOException {
            FileWriter writer = new FileWriter(path);
            for (List<String> record: records) {
                String collect = record.stream().collect(Collectors.joining(delimiter));
                writer.write(collect + "\n");
            }
            writer.close();
    }

    public Hashtable<String, String> dictFromCsv(String path, String delimiter) throws IOException {
        Hashtable<String, String> records = new Hashtable<String, String>();
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(delimiter);
                if (values.length == 2) {
                    records.put(values[0], values[1]);
                }
            }
            return records;
        }
    }
    
    public List<List<String>> intMethodsToStr(List<List<String>> csvdata, Hashtable<String, String> dictionary) throws IOException {
        int DEFINE_METHOD_INDEX = 4;
        int ANCHORING_METHOD_INDEX = 6;
        for (List<String> record: csvdata) {
            try {
                String defineMethodDictval = dictionary.get(record.get(DEFINE_METHOD_INDEX).split(" ")[1]);
                if (defineMethodDictval != null) {
                    record.set(DEFINE_METHOD_INDEX, defineMethodDictval);
                }
            } catch (Exception ArrayIndexOutOfBoundsException) {
                record.set(DEFINE_METHOD_INDEX, "different description");
            }

            try {
                String anchoringMethodDictval = dictionary.get(record.get(ANCHORING_METHOD_INDEX).split(" ")[1]);
                if (anchoringMethodDictval != null) {
                    record.set(ANCHORING_METHOD_INDEX, anchoringMethodDictval);
                }
            } catch (Exception ArrayIndexOutOfBoundsException) {
                record.set(ANCHORING_METHOD_INDEX, "no anchorage");
            }
        }
        return csvdata;
    }

    public int pointsQuantity(List<List<String>> csvdata) {
        return csvdata.size() - 1;
    }

    private BrokenLine brokenLineFromCsv(List<List<String>> csvdata) throws ParseException {
        List<Point> points = new ArrayList<>();
        for (int i = 1; i < csvdata.size(); i++) {
            List<String> record = csvdata.get(i);
            for (int j = 0; j < record.size(); j++) {
                NumberFormat format = NumberFormat.getInstance(Locale.getDefault());
                Number x_number = format.parse(record.get(2));
                Number y_number = format.parse(record.get(3));
                double x = x_number.doubleValue();
                double y = y_number.doubleValue();
                points.add(new Point(x, y));
            }
        }
        Point[] pointsArr = points.toArray(new Point[points.size()]);
        return new BrokenLine(pointsArr);
    }

    public double brokenLineLength(List<List<String>> csvdata) throws ParseException {
        BrokenLine br = brokenLineFromCsv(csvdata);
        return br.getLength();
    }

    public GeodesyPoint getGeodesyPointFromCsv(List<List<String>> inputCsvdata, int num) throws ParseException {
        double x;
        double y;
        for (int i = 1; i < inputCsvdata.size(); i++) {
            List<String> record = inputCsvdata.get(i);
            for (int j = 0; j < record.size(); j++) {
                NumberFormat format = NumberFormat.getInstance(Locale.getDefault());
                Number csvnum = format.parse(record.get(1));
                int intcsvnum = csvnum.intValue();
                if (intcsvnum == num) {
                    Number x_number = format.parse(record.get(2));
                    Number y_number = format.parse(record.get(3));
                    x = x_number.doubleValue();
                    y = y_number.doubleValue();
                    return new GeodesyPoint(x, y);
                }
            }
        }
        return null;
    }

    public List<List<String>> turnFigure(List<List<String>> inputCsvdata, int gpnumber, double angle) throws ParseException {
        GeodesyPoint gp = getGeodesyPointFromCsv(inputCsvdata, gpnumber);
        for (int i = 1; i < inputCsvdata.size(); i++) {
            List<String> record = inputCsvdata.get(i);
            for (int j = 0; j < record.size(); j++) {
                NumberFormat format = NumberFormat.getInstance(Locale.getDefault());
                Number x_number = format.parse(record.get(2));
                Number y_number = format.parse(record.get(3));
                double x = x_number.doubleValue();
                double y = y_number.doubleValue();
                GeodesyPoint tempgp =  new GeodesyPoint(x, y).turnPointRelatively(gp, angle);
                record.set(2, String.valueOf(tempgp.x));
                record.set(3, String.valueOf(tempgp.y));
            }
        }
        return inputCsvdata;
    }
}