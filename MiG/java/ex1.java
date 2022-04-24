import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;

public class ex1 {
    public static void main(String[] args) throws Exception {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        String help = "This programm create txt file in zip file.\n"
                    + "Please enter txt file name and zip name:";
        System.out.println(help); 
        String namef = bufferedReader.readLine(); 
        String namez = bufferedReader.readLine();
        if (namef.trim().length() == 0 || namez.trim().length() == 0) {
            System.out.println("Your insert is empty. Retype.");
            try {
                String s = null;
                Process p = Runtime.getRuntime().exec("python ex6.2.py --help");
                BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
                while ((s = stdInput.readLine()) != null) {
                    System.out.println(s);
                }
                System.exit(0);
            } catch (IOException e) {
                e.printStackTrace();  
            }
        }
        String command = String.format("python ex6.2.py --namef %s --namez %s", namef, namez);
        System.out.println(command);
        String s = null;
        try {
            Process p = Runtime.getRuntime().exec(command);
            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            System.out.println("Stdout:\n");
            while ((s = stdInput.readLine()) != null) {
                System.out.println(s);
            }
            System.out.println("Stderr:\n");
            while ((s = stdError.readLine()) != null) {
                System.out.println(s);
            }
            String result = "Succesed!";
            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
