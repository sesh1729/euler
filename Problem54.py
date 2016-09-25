
#Problem 144 
#Investigating multiple reflections of a laser beam

import math
def get_next_point(x1,y1,x2,y2):

    ellipse_equation = "4x^2 + y^2 = 100"
    m_i = (y2-y1)/(x2-x1)
    m_t = -4*x2/y2
    m_r = (2*m_t + m_t*m_t*m_i - m_i)/(1- m_t*m_t + 2*m_t*m_i)
    #print m_r
    #print math.atan(m_r)*180/3.14
    #print (2*math.atan(m_t) - math.atan(m_i))/(3.14+math.atan(m_r))
    x3 = (pow(m_r,2)*x2 - 4*x2 - 2*y2*m_r)/(4+pow(m_r,2))
    y3 = (4*y2 - 8*x2*m_r - pow(m_r,2)*y2)/(4+pow(m_r,2))
    return (x3,y3)


(x1,y1,x2,y2) = (0,10.1,1.4,-9.6)

counter = 1
while counter < 1000:
    counter = counter + 1
    (x3,y3) = get_next_point(x1,y1,x2,y2)
    if y3 > 0 and x3 >= -0.01 and x3 < 0.01:
        print counter, x3, y3
        break
    else:
        print counter, x3, y3
        (x1,y1) = (x2,y2)
        (x2,y2) = (x3,y3)

