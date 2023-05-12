use strict;
use warnings;
use 5.32.1;

select(STDOUT); $| = 1; # DO NOT REMOVE

chomp(my $n = <STDIN>);
chomp($n);

my %trie;
my $nb_elements = 0;  # number of elements (referencing a number) stored in the structure

for (my $i = 0; $i < $n; $i++) {
    my $phone_number = <>;
    chomp($phone_number);
    my $current_node = \%trie;

    foreach my $digit (split //, $phone_number) {
        if (exists $current_node->{$digit}) {
            $current_node = $current_node->{$digit};
        } else {
            $current_node->{$digit} = {};
            $current_node = $current_node->{$digit};
            $nb_elements++;
        }
    }
}

print "$nb_elements\n";
