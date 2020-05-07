public class HelloFenzhiXunhuan {
    public static void main(String[] args) {
        System.out.println("hello world!");
        int a = 3;
        while (a <= 5) {

            System.out.println(a);
            a++;// 与其他代码执行时 先执行原来的数
        }

        // 区别在于最少执行一次
        /*
         * int c = 8; do { System.out.println(c++); a++; } while (c<10);
         */
        int c = 8;
        do {
            System.out.println(c++);

        } while (c < 10);
        // for循环
        for (int b = 10; b < 15; b++) {
            System.out.println(b);
        }
        // if else分支
        int d = 3;
        if (d == 3) {
            System.out.println("d=3");

        } else if (d == 5) {
            System.out.println("d=4");
        } else {
            System.out.println("d不等于3也不等于4");
        }
        // switch分支
        int f = 3;
        switch (f) {
            case 1:
                System.out.println("你的成绩是A");
                break;
            case 2:
                System.out.println("你的成绩是B");
                break;
            case 3:
                System.out.println("你的成绩是C");
                break;
            default:
                System.out.println("你的成绩不及格！");
        }

    }
}