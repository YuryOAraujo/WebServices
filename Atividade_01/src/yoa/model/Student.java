package yoa.model;

public class Student {
	private String registrationNumber, name;
	private int age;
	
	public Student(String registrationNumber, String name, int age) {
		super();
		this.registrationNumber = registrationNumber;
		this.name = name;
		this.age = age;
	}

	public String getRegistrationNumber() {
		return registrationNumber;
	}

	public void setRegistrationNumber(String registrationNumber) {
		this.registrationNumber = registrationNumber;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public String toString() {
		return String.format("- %s, %d anos, matrícula %s", name, age, registrationNumber);
	}
	
	
}
