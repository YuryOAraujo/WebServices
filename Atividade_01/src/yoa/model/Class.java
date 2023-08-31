package yoa.model;

import java.util.ArrayList;
import java.util.List;

public class Class {
	private String classID, name;
	private int year;
	private List<Student> studentList;
	
	public Class(String classID, String name, int year) {
		this.classID = classID;
		this.name = name;
		this.year = year;
		studentList = new ArrayList<>();
	}
	
	public boolean addStudent(Student student) {
		studentList.add(student);
		return true;		
	}

	public String getClassID() {
		return classID;
	}

	public void setClassID(String classID) {
		this.classID = classID;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

	public List<Student> getStudentList() {
		return studentList;
	}

	public void setStudentList(List<Student> studentList) {
		this.studentList = studentList;
	}

	@Override
	public String toString() {
		StringBuilder stringBuilder = new StringBuilder();
		stringBuilder.append("Turma ").append(name).append(String.format(" (%d)", year)).append("\n");
		for(Student student:studentList)
			stringBuilder.append(student).append("\n");
		
		return stringBuilder.append("\n").toString();
	}
	
	
}
