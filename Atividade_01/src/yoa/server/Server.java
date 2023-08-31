package yoa.server;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

import yoa.model.Class;
import yoa.model.Student;

public class Server {
	public static void main(String[] args){
		try {
			startServer();
		} catch (IOException e) {
			e.printStackTrace();
		}


	}

	private static void startServer() throws IOException {
		int port = 12345;

		ServerSocket serverSocket = new ServerSocket(port);
		System.out.println("Server listening on port " + port);

		Socket clientSocket = serverSocket.accept();
		System.out.println("Client connected");

		PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
		out.println(displayData());
		System.out.println("Data sent, ending connection ...");

		serverSocket.close();
	}

	private static String displayData() {
		Class firstClass = new Class("1", "Turma 1", 2019);
		Class secondClass = new Class("2", "Turma 2", 2022);

		firstClass.addStudent(new Student("12345", "João da Silva", 22));
		firstClass.addStudent(new Student("45874", "Maria do Carmo", 18));
		firstClass.addStudent(new Student("98547", "Paulo Roberto", 20));
		firstClass.addStudent(new Student("54321", "Carlos Alberto", 19));
		firstClass.addStudent(new Student("87456", "Amanda Souza", 21));

		secondClass.addStudent(new Student("41258", "Roberto Carlos", 17));
		secondClass.addStudent(new Student("87459", "Juliana de Paula", 18));
		secondClass.addStudent(new Student("65478", "Lucas Santos", 19));
		secondClass.addStudent(new Student("98741", "Fernanda Oliveira", 20));
		secondClass.addStudent(new Student("25689", "Rafaela Mendes", 18));
		return new StringBuilder().append(firstClass).append(secondClass).toString();
	}
}