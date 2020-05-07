/*大小写敏感：这就意味着标识符 Hello 与 hello 是不同的。
类名：对于所有的类来说，类名的首字母应该大写。如果类名由若干单词组成，那么每个单词的首字母应该大写，例如 MyFirstJavaClass 。
方法名：所有的方法名都应该以小写字母开头。如果方法名含有若干单词，则后面的每个单词首字母大写。
源文件名：源文件名必须和类名相同。当保存文件的时候，你应该使用类名作为文件名保存（切记 Java 是大小写敏感的），文件名的后缀为 .java。（如果文件名和类名不相同则会导致编译错误）。
主方法入口：所有的 Java 程序由 public static void main(String []args) 方法开始执行。*/
public class HelloShujuleixing {
    // 合法标识符举例：age、$salary、_value、__1_value
    // 非法标识符举例：123abc、-salary
    public static void main(final String[] args) {
        System.out.println("hello world!");
        // 声明变量 基本数据类型
        // int 32位 long 64位L float 32位F double 64位 byte 8位 char 一个字符16位
        // boolean 01 String 字符串
        // 当声明变量不使用时会报错
        int a = 1;

        System.out.println(a);
        byte c = 127;

        System.out.println(c);
        boolean g = true;
        char b = 'a';

        System.out.println(b);
        System.out.println(g);
        double double2 = 3.4343;
        System.out.println(double2);

        float float2 = 322.4444F;
        System.out.println(float2);
        String string2 = "i love you";
        System.out.println(string2);
        long long2 = 3434455L;
        System.out.println(long2);
        // 函数方法的调用 执行代码放在main接口里面
        cook();
        // 数组声明
        int[] ints = { 1, 3, 4, 5, 6, 7 };

        System.out.println(ints);
        char[] fdfk = { 'a', 'b', 'c', 'd' };
        System.out.println(fdfk);

    }

    // 函数方法的声明
    public static void cook() {
        System.out.println("切菜");
        System.out.println("做饭");
        System.out.println("吃饭");

    }
}