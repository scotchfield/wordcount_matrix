import optparse
import os
import re
import string
import sys


"""
Open the file located at input_filename and return a dictionary where the
set of keys are the individual (stripped) terms and the values are the
number of occurrences.

For example, a file containing the text "Hello world" would return a dict
of the form { 'hello': 1, 'world': 1 }.

re_pattern_nospace is a regex describing the characters that should be
replaced by the empty string. re_pattern describes the characters that
should be replaced by a single space.
"""
def get_word_count( input_filename ):
    word_obj = {}

    re_pattern_nospace = re.compile( '[\'_]+' )
    re_pattern = re.compile( '[^A-Za-z0-9_\']+' )

    input_file = open( input_filename, 'r' )
    input_data = [ line.strip().lower() for line in input_file ]
    input_data = [
        re_pattern_nospace.sub( '', line ) for line in input_data ]
    input_data = [ re_pattern.sub( ' ', line ) for line in input_data ]
    input_data = [ line.split( ' ' ) for line in input_data ]

    for word_line in input_data:
        for word in word_line:
            if len( word ) > 0:
                word_obj[ word ] = word_obj.get( word, 0 ) + 1

    input_file.close()
    return word_obj

def get_files( directory, match ):
    obj = []
    for ( root, _, filenames ) in os.walk( directory ):
        for filename in filenames:
            if match in filename:
                obj.append( os.path.join( root, filename ) )
    return sorted( obj )

def main():
    parser = optparse.OptionParser( 'Usage: python wordcount_matrix.py args' )
    parser.add_option( '-d', '--directory', dest='directory',
                       default='.', type='string',
                       help='The source directory' )
    parser.add_option( '-f', '--file_mask', dest='file_mask',
                       default='', type='string',
                       help='The files to parse (ex: -f .php)' )
    parser.add_option( '-o', '--output_file', dest='output_file',
                       type='string',
                       help='The output file to write to.' )

    (options, args) = parser.parse_args()

    file_obj = get_files( options.directory, options.file_mask )

    if not options.output_file:
        output_file = sys.stdout
    else:
        output_file = open( options.output_file, 'w' )

    file_word_obj = {}
    all_word_obj = {}

    for file_name in file_obj:
        word_obj = get_word_count( file_name )
        for word in word_obj:
            all_word_obj[ word ] = True
        file_word_obj[ file_name ] = word_obj

    words = sorted( all_word_obj.keys() )
    output_file.write( '_filename_,{0}\n'.format( ','.join( words ) ) )

    for file_name in file_obj:
        output_obj = []
        word_obj = file_word_obj[ file_name ]
        for w in words:
            output_obj.append( str( word_obj.get( w, '0' ) ) )
        output_file.write( '{0},{1}\n'.format( file_name,
                                               ','.join( output_obj ) ) )

    if options.output_file:
        output_file.close()


if __name__ == "__main__":
    main()
