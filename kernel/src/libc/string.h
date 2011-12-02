
#define __expect(foo,bar) (foo)
#define __likely(foo) __expect((foo),1)
#define __unlikely(foo) __expect((foo),0)

#define size_t unsigned int

void* memset(void * dst, int s, size_t count);
void *memcpy (void *dst, const void *src, size_t n);
void *memmove(void *dst, const void *src, size_t count);
size_t strlen(const char *s);
