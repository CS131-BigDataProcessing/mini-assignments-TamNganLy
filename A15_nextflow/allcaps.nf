#!/usr/bin/env nextflow

workflow {
    inputChannel = Channel.of(params.inputString)
    result = convertToUppercase(inputChannel) 
    result.view { println it }
}

process convertToUppercase {
    input:
    val inputString  // The input string

    output:
    stdout  // Capture the output of the command to standard output

    script:
    """
    echo "${inputString.toUpperCase()}"
    """
}
