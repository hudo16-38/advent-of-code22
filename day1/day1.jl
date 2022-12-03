function split_input(file_name::String)::Vector{Vector{String}}

    buckets = []

    open(file_name) do f
        lines = readlines(f)
        bucket = []

        for line in lines
            if line == ""
                append!(buckets, bucket)
                bucket = []
            else
                #value = parse(Int, line)
                append!(bucket, value)
            end
        end
    end
    return buckets     
end

buckets = split_input("test_input.txt")


