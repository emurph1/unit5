#Emily Murphy
#2017-11-29
#combSort.py - sorting algorithim

"""function combsort(array input)

    gap := input.size // Initialize gap size
    shrink := 1.3 // Set the gap shrink factor
    sorted := false

    loop while sorted = false
        // Update the gap value for a next comb
        gap := floor(gap / shrink)
        if gap > 1
            sorted := false // We are never sorted as long as gap > 1
        else
            gap := 1
            sorted := true // If there are no swaps this pass, we are done
        end if

        // A single "comb" over the input list
        i := 0
        loop while i + gap < input.size // See Shell sort for a similar idea
            if input[i] > input[i+gap]
                swap(input[i], input[i+gap])
                sorted := false
                // If this assignment never happens within the loop,
                // then there have been no swaps and the list is sorted.
             end if

             i := i + 1
         end loop
         
     end loop
 end function """
 
 def mySort(A):
     gap = N
     shrink = 1.3
     sort = False
     while sort = False:
         gap = floor(gap/shrink)
        if gap > 1:
            sort = False
        else:
            gap = 1
            sort = True
            
        i = 0
        while i + gap < N:
            if [i] > [i+gap]:
                [i], [i+gap] = [i+gap], [i]
                sort = False
            i += 1
