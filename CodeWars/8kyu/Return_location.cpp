/*
You are given a class named Person, which has the variables m_x, m_y, m_z — coordinates of some 3D location — and a method named location, which should transfer these coordinates to the three arguments of the function — x, y, z.

Consider this example:

  Person person(1, 2, 3);      // m_x = 1, m_y = 2, m_z = 3
  int x = 0, y = 0, z = 0;
  person.location(x, y, z);    /* x = m_x = 1;
                                  y = m_y = 2;
                                  z = m_z = 3;
                               */
Can you find the bug?

FundamentalsDebugging
*/