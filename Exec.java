import java.io.*;

public class Exec 
{
   public static void main(String[] args) throws IOException {
       Process p = Runtime.getRuntime().exec(args[0]);
       byte[] b = new byte[1];
       while (p.getErrorStream().read(b) > 0)
           System.out.write(b);
       while (p.getInputStream().read(b) > 0)
           System.out.write(b);
   }
}
