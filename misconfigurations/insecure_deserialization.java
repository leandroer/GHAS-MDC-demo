// Insecure Deserialization
import java.io.*;

public class InsecureDeserialization {
    
    public static Object deserializeUserInput(String serializedData) throws IOException, ClassNotFoundException {
        // VULNERABILITY: Deserializing untrusted data can lead to RCE
        ByteArrayInputStream bais = new ByteArrayInputStream(serializedData.getBytes());
        ObjectInputStream ois = new ObjectInputStream(bais);
        Object obj = ois.readObject();
        ois.close();
        return obj;
    }
    
    public static void main(String[] args) throws Exception {
        String userInput = args[0];
        // Directly deserializing user input
        Object obj = deserializeUserInput(userInput);
        System.out.println(obj);
    }
}
