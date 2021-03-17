package com.company;

import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class AlgoHT {
    public static void main(String[] args) throws Throwable {
        File f1 = new File("input.txt");
        FileWriter f2 = new FileWriter("output.txt");
        Scanner scanner = new Scanner(f1);
        Queue q = new Queue(Integer.parseInt(scanner.nextLine()));

        String line;
        try {
            while(scanner.hasNextLine()){
                line = scanner.nextLine();
                if(line.contains("+"))
                    q.push(Integer.parseInt(line.substring(line.lastIndexOf(' ')+1)));
                if(line.contains("-"))
                    q.pop();
                if(line.contains("?"))
                    f2.write(q.getMin()+"\n");
            }
        }catch (Throwable t) {
            t.printStackTrace();
        }finally {
            f2.close();
        }
    }
    static class Queue{
        private final int[] array;
        private int start;
        private int end;
        private int minPos;
        private int size;

        Queue(int size){
            array = new int[size];
        }
        void push(int a) throws Throwable{
            array[end] = a;
            size++;

            if(array[minPos]>=a)
                minPos = end;

            end++;
            if(end == array.length)
                end = 0;
            if(end == start && size!=0)
                throw new Throwable("Out of range");
        }
        int pop() throws Throwable{
            int res = array[start];
            size--;

            start++;
            if(start-1 == minPos)
                minPos = findNewMin();

            if(start == array.length)
                start = 0;
            if(start == end && size!=0)
                throw new Throwable("Out of range");
            return res;
        }

        private int findNewMin() {
            int minPos = start;
            for (int i = start; i < ((start > end)?array.length:end); i++)
                if(array[i] < array[minPos])
                    minPos = i;
            if(start > end)
                for (int i = 0; i < end; i++)
                    if(array[i] < array[minPos])
                        minPos = i;
            return minPos;
        }

        int getMin(){
            return array[minPos];
        }
    }
}
